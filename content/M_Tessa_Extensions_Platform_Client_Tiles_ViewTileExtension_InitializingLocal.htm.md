# ViewTileExtension.InitializingLocal - метод
Выполняет добавление, удаление и настройку плиток в локальной рабочей области,
которая определяется как копия глобальной рабочей области.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Tiles](N_Tessa_Extensions_Platform_Client_Tiles.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task InitializingLocal(
    	ITileLocalExtensionContext context
    )
VB __Копировать
     Public Overrides Function InitializingLocal ( 
    	context As ITileLocalExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ InitializingLocal(
    	ITileLocalExtensionContext^ context
    ) override
F# __Копировать
     abstract InitializingLocal : 
            context : ITileLocalExtensionContext -> Task 
    override InitializingLocal : 
            context : ITileLocalExtensionContext -> Task 
#### Параметры
context
[ITileLocalExtensionContext](T_Tessa_UI_Tiles_Extensions_ITileLocalExtensionContext.htm)
    Контекст расширений для наполнения локальной рабочей области с панелями плиток.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ITileLocalExtension.InitializingLocal(ITileLocalExtensionContext)](M_Tessa_UI_Tiles_Extensions_ITileLocalExtension_InitializingLocal.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[ViewTileExtension -
](T_Tessa_Extensions_Platform_Client_Tiles_ViewTileExtension.htm)
[Tessa.Extensions.Platform.Client.Tiles - пространство
имён](N_Tessa_Extensions_Platform_Client_Tiles.htm)
