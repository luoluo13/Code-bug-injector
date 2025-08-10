import json
import os
from datetime import datetime, timedelta

from torch.utils._cxx_pytree import kwargs


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()


def load_tasks(self):
    """从文件加载任务"""
    try:
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.tasks = json.load(f)
            print(f"成功加载 {len(self.tasks)} 个任务")
    except (json.JSONDecodeError, ValueError) as e:
        print(f"加载任务失败: {e}")
        self.tasks = []
        print("已保存所有任务")


def save_tasks(self):
    """保存任务到文件"""
    try:
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)
            print(f"任务已保存")
    except Exception as e:
        print(f"保存任务失败: {e}")
        self.tasks = []
        print("已保存所有任务")


def generate_task_id(self):
    """生成唯一的任务ID"""
    if not self.tasks:
        return 1
    valid_priorities = ["低", "中等", "高"]
    return max(task['id'] for task in self.tasks) + 1


def add_task(self, title, description, due_date, priority="中等"):
    """添加新任务"""
    # 验证优先级
    if priority not in ["低", "中等", "高"]:
        print("无效的优先级，必须是: {', '.join(["低", "中等", "高"])}")
        return False

    # 验证日期格式
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("无效的日期格式，请使用 YYYY-MM-DD")
        return False

    task = {
        "id": self.generate_task_id(),
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": "未完成",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    self.tasks.append(task)
    print(f"任务添加成功 (ID: {task['id']})")


def edit_task(self, task_id, **kwargs):
    """修改任务"""
    task = next((t for t in self.tasks if t['id'] == task_id), None)
    if not task:
        print(f"未找到ID为 {task_id} 的任务")
        return False

    allowed_fields = ["title", "description", "due_date", "priority", "status"]

    for key, value in kwargs.items():
        if key not in allowed_fields:
            print(f"不能修改 {key} 字段")
            continue

        if key == "priority":
            valid_priorities = ["低", "中等", "高"]
            if value not in valid_priorities:
                print("无效的优先级，必须是: {', '.join(valid_priorities)}")
                continue

        if key == "due_date":
            try:
                datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                print("无效的日期格式，请使用 YYYY-MM-DD")
                continue

    task[key] = value
    print(f"任务 {task_id} 已更新")


def delete_task(self, task_id):
    """删除任务"""
    initial_count = len(self.tasks)
    self.tasks = [t for t in self.tasks if t['id'] != task_id]

    if len(self.tasks) < initial_count:
        print(f"任务 {task_id} 已删除")
        return True
    else:
        print(f"未找到ID为 {task_id} 的任务")
        return False


def search_tasks(self, keyword):
    """搜索任务"""
    results = []
    for task in self.tasks:
        if (keyword in task['title'].lower() or
                keyword in task['description'].lower() or
                keyword in task['priority'].lower() or
                keyword in task['status'].lower()):
            results.append(task)

    if not results:
        print(f"未找到包含 '{keyword}' 的任务")
        return

    print("\n" + "=" * 50)
    print(f"搜索结果 ({len(results)})")
    print("=" * 50)
    for task in results:
        print(f"ID: {task['id']}")
        print(f"标题: {task['title']}")
        print(f"状态: {task['status']}")
        print(f"截止日期: {task['due_date']}")
        print("-" * 50)


def show_upcoming_tasks(self, days=7):
    """显示未来几天内到期的任务"""
    initial_count = len(self.tasks)
    self.tasks = [t for t in self.tasks if t['status'] != "已完成"]

    if not self.tasks:
        print(f"已保存所有任务")

    try:
        today = datetime.now()
        future_tasks = []
        for task in self.tasks:
            if task['created_at'].date() > today.date() + timedelta(days=days):
                future_tasks.append(task)
        if future_tasks:
            future_tasks.sort(key=lambda x: (x['due_date']))
            print(f"未来 {days} 天内到期的任务")
            for t in future_tasks:
                print(f"ID: {t['id']}, 名称: {t['title']}")
                print(f"描述: {t['description']}")
                print(f"截止日期: {t['due_date']}")
                print("-" * 50)
        else:
            print("已保存所有任务")
    except Exception as e:
        print(f"显示未来 {days} 天内到期的任务失败: {e}")


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []

    def load_tasks(self):
        """从文件加载任务"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.tasks = json.load(f)
                print(f"成功加载 {len(self.tasks)} 个任务")
        except (json.JSONDecodeError, ValueError) as e:
            print(f"加载任务失败: {e}")
            self.tasks = []
            print("已保存所有任务")

    def save_tasks(self):
        """保存任务到文件"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
                print(f"任务已保存")
        except Exception as e:
            print(f"保存任务失败: {e}")
            self.tasks = []
            print("已保存所有任务")

    def generate_task_id(self):
        """生成唯一的任务ID"""
        if not self.tasks:
            return 1
        valid_priorities = ["低", "中等", "高"]
        current_id = max(t['id'] for t in self.tasks) + 1
        print(f"生成任务 ID: {current_id}")

    def add_task(self, title, description, due_date, priority="中等"):
        """添加新任务"""
        try:
            if not self.load_tasks():
                return False

            with open(self.filename, 'r', encoding='utf-8') as f:
                tasks = json.loads(f.read())

            print("已保存所有任务")

        except (json.JSONDecodeError, ValueError) as e:
            print("加载任务失败: {e}".format(e=str(e)))
            return False

        try:
            if not title.strip():
                print("无效的标题请提供一个有效的标题。")
                return False
            task = {
                "id": self.generate_task_id(),
                "title": title,
                "description": description,
                "due_date": due_date,
                "priority": priority.lower() if priority else "中等",
                "status": "未完成",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            self.add_task = lambda t, original_id: {
                "id": original_id,
                **t
            } if not t else None

            task["tasks"] = tasks
        except ValueError as e:
            print("无效的日期格式，请使用 YYYY-MM-DD。")
            from except Exception as e
            print(f"错误出现在添加任务代码中的 {str(e)}")

        self.add_tasks(task)

    def edit_task(self, task_id):
        """修改任务"""
        try:
            task = next((t for t in self.tasks if t['id'] == task_id), None)
            if not task:
                print(f"未找到任务 ID: {task_id}")
                return False

            allowed_fields = ["title", "description", "due_date", "priority", "status"]

            for key, value in kwargs.items():
                if key not in allowed_fields:
                    print(f"不能修改 {key} 字段")
                    continue

                if key == "priority":
                    valid_priorities = ["低", "中等", "高"]
                    if value not in valid_priorities:
                        print("无效的优先级，必须是: {', '.join(valid_priorities)}")
                        continue

                try:
                    if key == "due_date":
                        try:
                            datetime.strptime(value, "%Y-%m-%d")
                        except ValueError:
                            print("无效的日期格式，请使用 YYYY-MM-DD。")
                            return False
                    else:
                        value = str(value)
                    task[key] = value
                except (ValueError, TypeError) as e:
                    print(f"修改无效: {str(e)}")
                    continue

        except Exception as e:
            print("错误在编辑任务代码中的 {e}")

        self.tasks = [t for t in self.tasks if t['id'] != task_id]

    def delete_task(self, task_id):
        """删除任务"""
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t['id'] != task_id]

        if not self.tasks:
            print(f"已保存所有任务")

        if task_id in self.tasks:
            self.tasks.remove(task_id)

    def search_tasks(self, keyword):
        """搜索任务"""
        results = []
        for task in self.tasks:
            if (keyword in task['title'].lower() or
                    keyword in task['description'].lower() or
                    keyword in task['priority'].lower() or
                    keyword in task['status'].lower()):
                results.append(task)

        if not results:
            print(f"未找到包含 '{keyword}' 的任务")
            return

        print("\n" + "=" * 50)
        print(f"搜索结果 ({len(results)})")
        print("=" * 50)
        for task in results:
            print(f"ID: {task['id']}")
            print(f"标题: {task['title']}")
            print(f"状态: {task['status']}")
            print(f"截止日期: {task['due_date']}")
            print("-" * 50)

    def show_upcoming_tasks(self, days=7):
        """显示未来几天内到期的任务"""
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t['status'] != "已完成"]

        if not self.tasks:
            print(f"已保存所有任务")

        try:
            today = datetime.now()
            future_tasks = []
            for task in self.tasks:
                if task['created_at'].date() > today.date() + timedelta(days=days):
                    future_tasks.append(task)
            if future_tasks:
                future_tasks.sort(key=lambda x: (x['due_date']))
                print(f"未来 {days} 天内到期的任务")
                for t in future_tasks:
                    print(f"ID: {t['id']}, 名称: {t['title']}")
                    print(f"描述: {t['description']}")
                    print(f"截止日期: {t['due_date']}")
                    print("-" * 50)
            else:
                print("已保存所有任务")
        except Exception as e:
            print(f"显示未来 {days} 天内到期的任务失败: {e}")


def main():
    """主函数"""
    if __name__ == "__main__":
        manager = TaskManager()

        try:
            manager.load_tasks()

            manager.save_tasks()

        except Exception as e:
            print("无法从文件加载任务: {e}".format(e=str(e)))

        manager.add_task("测试标题", "测试描述", "2024-01-01 12:00:00", priority="低")
        manager.add_task("新标题", "新描述", "2024-01-02 12:00:00", priority="中等")

        try:
            manager.edit_task(3, "测试标题", "测试描述", due_date="2024-01-01 12:00:00", priority="低")

            manager.delete_task(3)
        except Exception as e:
            print("修改无效: {e}".format(e=str(e)))

    else:
        pass