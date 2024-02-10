from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import types

import app.keyboards as kb
from app.database.requests import get_product

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Wellcome", reply_markup=kb.main)

@router.message(F.text == 'click me')
async def catalog(message: Message):
    await message.answer('choose', reply_markup=await kb.categories())

@router.message(F.text == 'about')
async def catalog(message: Message):
    url = 'https://github.com/kokakoalla/tele_bot5/blob/master/README.md'
    text = f"{url}"
    await message.answer(text)


@router.callback_query(F.data.startswith('category_'))
async def category_selected(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]
    await callback.message.answer(f'choose', reply_markup=await kb.products(category_id))
    await callback.answer('')

@router.callback_query(F.data.startswith('product_'))
async def product_selected(callback: CallbackQuery):
    product_id = callback.data.split('_')[1]
    product = await get_product(product_id)
    await callback.message.answer(product.description)
    await callback.answer('')