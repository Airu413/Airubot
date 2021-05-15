import discord
from discord.ext.commands import Bot

intents=discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} 에 로그인하였습니다!')

@bot.command()
async def 안녕(ctx):
    await ctx.send('만나서 반갑다냥!')

@bot.command()
async def 아이루봇(ctx):
    await ctx.send(embed=embed)

embed = discord.Embed(title='아이루봇 설명서',description='나를 소개해주겠다냥!', color = 0x00ff00)
embed.add_field(name='몬스터 설명',value='!몬스터 이름 으로 몬스터의 간단한 정보를 볼 수 있다냥! 몬스터 이름을 적을 때는 기호를 빼고 적어달라냥 (예시:테오-테스카토르X 테오테스카토르O)', inline=True)

@bot.command()
async def 테오테스카토르(ctx):
    await ctx.send('염왕룡(炎王龍)')
    await ctx.send('불꽃의 왕 테오-테스카토르')
    await ctx.send('위험도 8/10')
    await ctx.send('움직인 자리나 공격한 곳에 분진이 남고 일정 시간 후 폭발한다냥! 필살기는 몸에 두른 분진을 한번에 폭파시키는 기술, 맞으면 쓰러질 확률이 매우 높으니 주의하자냥! 머리를 파괴하면 폭발의 규모가 작아진다냥!')
    await ctx.send('염룡의 보옥-머리 파괴 3%')
    await ctx.send('타겟 3%')
    await ctx.send('갈무리 2%')
    await ctx.send('꼬리 갈무리 3%')
    await ctx.send('유실물 1%')

@bot.command()
async def 바젤기우스(ctx):
    await ctx.send('폭린룡(爆鱗竜)')
    await ctx.send('기습하는 불의 벌판 바젤기우스')
    await ctx.send('공격하거나 머리를 흔들 때 폭발 비늘을 뿌린다냥! 비늘은 일정 시간 후 붉어지면서 폭발하고 분노 상태에서는 비늘이 바로 폭발하지만 대신 일부 육질이 연해진다냥! 필살기는 하늘로 날아올라 두번 왕복하며 비늘을 떨어트린 뒤 급강하로 공격하는 패턴이다냥!')
    await ctx.send('폭린룡의 보옥-타겟 2%')
    await ctx.send('포획 3%')
    await ctx.send('머리 파괴 3%')
    await ctx.send('등 파괴 1%')
    await ctx.send('유실물 1%')

@bot.command()
async def 오나즈치(ctx):
    await ctx.send('하룡(霞龍)')
    await ctx.send('고대의 환영 오나즈치')
    await ctx.send('위험도 8/10')
    await ctx.send('은신 상태에서는 일부 육질이 연해지고 데미지를 쌓으면 특수 대경직과 은신 해제를 볼 수 있고 뿔과 꼬리를 자르면 투명화가 약해진다냥! 맹독을 이용한 공격을 하는데 독구슬을 뱉거나 독 브레스를 쓰고, 필살기는 브레스를 사방으로 흩뿌리는 패턴이다냥!')
    await ctx.send('하룡의 보옥-유실물 1%')
    await ctx.send('갈무리 2%')
    await ctx.send('뿔 파괴 3%')
    await ctx.send('타겟 3%')

@bot.command()
async def 크샬다오라(ctx):
    await ctx.send('강룡(鋼龍)')
    await ctx.send('폭풍 속에서 춤추는 그림자 크샬다오라')
    await ctx.send('위험도 8/10')
    await ctx.send('몸에 바람을 둘러 마지막에는 검은 용풍압 상태가 된다냥! 몸 주변에 거대한 회오리를 생성하는 필살기 이후에는 몸에 두른 바람이 약해지고, 데미지를 일정량 누적하거나 독 상태에 걸리게 하면 용 풍압이 약해진다냥!')
    await ctx.send('강룡의 보옥-타겟 3%')
    await ctx.send('유실물 1%')
    await ctx.send('꼬리 갈무리	3%')
    await ctx.send('갈무리 2%')
    await ctx.send('머리 파괴 3%')

@bot.command()
async def 나루하타타히메(ctx):
    await ctx.send('뇌신룡(雷神龍)')
    await ctx.send('재앙의 천둥 나루하타타히')
    await ctx.send('위험도 10/10')
    await ctx.send('공중에 떠있는 지면 위의 공성병기로 공격하자냥! 주로 고리, 구체 등의 형태로 번개를 발사하는 공격을 하고 필살기는 땅 전체에 광범위 피해를 주는 공격을 한다냥! 생겨난 지면 위로 올라가면 필살기를 회피할 수 있다냥! 3페이즈로 나뉘어 있는데 2페이즈 시작시 파룡포, 3페이즈 시작시 격룡창이 등장한다냥! 경직이나 특정 패턴마다 노출하는 복부의 발전기관을 공략하자냥!')
    await ctx.send('뇌신의 용옥-뿔 파괴 3%')
    await ctx.send('유실물 1%')
    await ctx.send('꼬리 갈무리	3%')
    await ctx.send('갈무리 1%')
    await ctx.send('복부 파괴 3%')
    await ctx.send('타겟 2%')

@bot.command()
async def 이부시마키히코(ctx):
    await ctx.send('풍신룡(風神龍)')
    await ctx.send('재앙의 숨결 이부시마키히코')
    await ctx.send('위험도 9/10')
    await ctx.send('(2.0) 백룡아행으로만 싸울 수 있는 몬스터다냥! 등장하자마자 첫번째 관문을 한번에 부수니 최종 관문의 준비를 철저히 하자냥! 몸 여기저기에 빨간 빛이 나는 바람주머니를 공략하자냥! 주의해야 할 공격은 바위 여러 개를 공중에 띄운 뒤 전부 관문에 날려 엄청난 데미지를 주는 공격이다냥! 이 공격을 막기 위해서는 공성병기로 공중의 바위를 모두 파괴하거나 파룡포를 쓰면 된다냥!')
    await ctx.send('풍신의 용옥-갈무리 1%')
    await ctx.send('꼬리 갈무리 3%')
    await ctx.send('유실물 1%')
    await ctx.send('타겟 2%')
    await ctx.send('뿔 파괴 3%')


bot.run('ODQxMjkwNDE1ODczMzI3MTY1.YJkmwQ.7nvWwO2Kwpoi77NmsauHgtdCRpA')
