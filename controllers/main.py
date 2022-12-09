# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Customer(http.Controller):
    @http.route('/get_customer', type='json', auth='user')
    def get_customer(self):
        customer_rec = request.env['res.partner'].search([])
        customer = []
        for rec in customer_rec:
            vals = {
                "id": rec.id,
                "name": rec.name,
            }
            customer.append(vals)
        data = {'status': 200, 'response': customer, 'message': 'Success'}
        return data

    @http.route('/create_customer', type='json', auth='user')
    def create_customer(self, **rec):
        if request.jsonrequest:
            if rec['name']:
                vals = {
                    'name': rec['name']
                }
                new_customer = request.env['res.partner'].sudo().create(vals)
                args = {'success': True, 'message': 'Success', 'ID': new_customer.id}
        return args

    @http.route('/update_customer', type='json', auth='user')
    def update_customer(self, **rec):
        if request.jsonrequest:
            if rec['id']:
                customer = request.env['res.partner'].sudo().browse(rec['id'])
                if customer:
                    customer.sudo().write(rec)
                args = {'success': True, 'message': 'Success'}
                return args

    @http.route('/delete_customer', type='json', auth='user')
    def delete_customer(self, **rec):
        if request.jsonrequest:
            if rec['id']:
                customer = request.env['res.partner'].sudo().browse(rec['id'])
                if customer:
                    customer.sudo().unlink()
                args = {'success': True, 'message': 'Success'}
                return args

