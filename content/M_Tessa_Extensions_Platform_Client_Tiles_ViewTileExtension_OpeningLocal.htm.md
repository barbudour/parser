# ViewTileExtension.OpeningLocal - метод
Выполняет подготовку локальной рабочей области для отображения одной из её
панелей.
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Tiles](N_Tessa_Extensions_Platform_Client_Tiles.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task OpeningLocal(
    	ITilePanelExtensionContext context
    )
VB __Копировать
     Public Overrides Function OpeningLocal ( 
    	context As ITilePanelExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ OpeningLocal(
    	ITilePanelExtensionContext^ context
    ) override
F# __Копировать
     abstract OpeningLocal : 
            context : ITilePanelExtensionContext -> Task 
    override OpeningLocal : 
            context : ITilePanelExtensionContext -> Task 
#### Параметры
context
[ITilePanelExtensionContext](T_Tessa_UI_Tiles_Extensions_ITilePanelExtensionContext.htm)
    Контекст расширений для управления отображением панели с плитками в локальной рабочей области.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ITilePanelExtension.OpeningLocal(ITilePanelExtensionContext)](M_Tessa_UI_Tiles_Extensions_ITilePanelExtension_OpeningLocal.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[ViewTileExtension -
](T_Tessa_Extensions_Platform_Client_Tiles_ViewTileExtension.htm)
[Tessa.Extensions.Platform.Client.Tiles - пространство
имён](N_Tessa_Extensions_Platform_Client_Tiles.htm)
