import sys
import pygame


def main():
    pygame.init()  # 初始化pygame
    size = width, height =  640, 480  # 设置窗口大小
    screen = pygame.display.set_mode(size)  # 显示窗口
    color = (0, 0, 0)  # 设置颜色
    ball = pygame.image.load(r"G:\domon\img\ball.png")  # 加载图片
    ball_rect = ball.get_rect()  # 获取矩形区域

    speed = [5, 5]  # 移动的像素距离

    clock = pygame.time.Clock()  # 设置时钟

    while True:  # 窗口循环
        clock.tick(60)  # 每秒执行60次
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ball_rect = ball_rect.move(speed)  # 移动小球

        # 碰到左右边缘
        if ball_rect.left < 0 or ball_rect.right > width:
            speed[0] = -speed[0]
        # 碰到上下边缘
        if ball_rect.top < 0 or ball_rect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(color)  # 填充颜色
        screen.blit(ball, ball_rect)  # 将图片画倒窗口上
        pygame.display.flip()  # 更新画面
    pygame.quit()




if __name__ == '__main__':
    main()



