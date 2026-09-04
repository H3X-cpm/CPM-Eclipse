#!/usr/bin/env python3
# server.py - CPM Eclipse Backend Server (Local Testing)
# Version: 4.8.2
# Author: H3X

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import datetime
import secrets

app = Flask(__name__)
CORS(app)

# ============================================
# DATABASE (Simple JSON file)
# ============================================

DATA_FILE = "users.json"

def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=2)

# ============================================
# API ENDPOINTS
# ============================================

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "CPM Eclipse Backend Server",
        "version": "4.8.2",
        "author": "H3X"
    })

@app.route('/api/verify', methods=['POST'])
def verify():
    """Verify user access key and points"""
    data = request.json
    key = data.get('key')
    action = data.get('action')
    
    users = load_users()
    
    for user_id, user_data in users.items():
        if user_data.get('access_key') == key:
            points = user_data.get('points', 0)
            cost = get_action_cost(action)
            
            if points >= cost:
                user_data['points'] = points - cost
                save_users(users)
                return jsonify({
                    "valid": True,
                    "can_use": True,
                    "remaining": user_data['points'],
                    "username": user_data.get('username', 'Unknown'),
                    "tier": user_data.get('tier', 'free'),
                    "message": "Points deducted successfully"
                })
            else:
                return jsonify({
                    "valid": True,
                    "can_use": False,
                    "remaining": points,
                    "username": user_data.get('username', 'Unknown'),
                    "tier": user_data.get('tier', 'free'),
                    "message": f"Insufficient points. Need {cost}, have {points}"
                })
    
    return jsonify({
        "valid": False,
        "error": "Invalid access key"
    })

@app.route('/api/stats', methods=['POST'])
def stats():
    """Get user stats"""
    data = request.json
    key = data.get('key')
    
    users = load_users()
    
    for user_id, user_data in users.items():
        if user_data.get('access_key') == key:
            return jsonify({
                "username": user_data.get('username', 'Unknown'),
                "points": user_data.get('points', 0),
                "tier": user_data.get('tier', 'free'),
                "created": user_data.get('created', 'Unknown'),
                "total_spent": user_data.get('total_spent', 0)
            })
    
    return jsonify({"error": "Invalid key"})

@app.route('/api/register', methods=['POST'])
def register():
    """Register new user"""
    data = request.json
    username = data.get('username')
    telegram_id = data.get('telegram_id')
    
    users = load_users()
    
    if telegram_id in users:
        return jsonify({"error": "User already exists"})
    
    access_key = secrets.token_hex(16)
    users[telegram_id] = {
        "username": username,
        "telegram_id": telegram_id,
        "access_key": access_key,
        "points": 0,
        "tier": "free",
        "created": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "total_spent": 0
    }
    
    save_users(users)
    
    return jsonify({
        "success": True,
        "access_key": access_key,
        "message": "User registered successfully"
    })

@app.route('/api/add_points', methods=['POST'])
def add_points():
    """Admin: Add points to user"""
    data = request.json
    admin_key = data.get('admin_key')
    user_id = data.get('user_id')
    amount = data.get('amount', 0)
    
    if admin_key != "th141206!":
        return jsonify({"error": "Unauthorized"})
    
    users = load_users()
    
    if user_id not in users:
        return jsonify({"error": "User not found"})
    
    users[user_id]['points'] = users[user_id].get('points', 0) + amount
    save_users(users)
    
    return jsonify({
        "success": True,
        "new_balance": users[user_id]['points'],
        "message": f"Added {amount} points"
    })

@app.route('/api/list_users', methods=['POST'])
def list_users():
    """Admin: List all users"""
    data = request.json
    admin_key = data.get('admin_key')
    
    if admin_key != "th141206!":
        return jsonify({"error": "Unauthorized"})
    
    users = load_users()
    user_list = []
    
    for user_id, user_data in users.items():
        user_list.append({
            "user_id": user_id,
            "username": user_data.get('username', 'Unknown'),
            "points": user_data.get('points', 0),
            "tier": user_data.get('tier', 'free')
        })
    
    return jsonify({"users": user_list})

def get_action_cost(action):
    """Get cost for each action"""
    costs = {
        "money": 10,
        "xp": 10,
        "vehicle": 25,
        "all_cars": 50,
        "rank": 20,
        "horns": 15,
        "houses": 20,
        "smoke": 15,
        "wheels": 20,
        "w16": 30
    }
    return costs.get(action, 10)

# ============================================
# RUN SERVER
# ============================================

if __name__ == '__main__':
    print("╔════════════════════════════════════════════╗")
    print("║         🌙 CPM ECLIPSE BACKEND            ║")
    print("║         Version: 4.8.2                    ║")
    print("║         Status: Running                   ║")
    print("║         Author: H3X                       ║")
    print("╚════════════════════════════════════════════╝")
    print("")
    print("📱 Server is running on: http://localhost:5000")
    print("🔑 Admin Secret Key: th141206!")
    print("")
    print("📋 Available Endpoints:")
    print("   GET  /                 - Home page")
    print("   POST /api/verify       - Verify user")
    print("   POST /api/stats        - Get stats")
    print("   POST /api/register     - Register user")
    print("   POST /api/add_points   - Add points (admin)")
    print("   POST /api/list_users   - List users (admin)")
    print("")
    app.run(host='0.0.0.0', port=5000, debug=False)
