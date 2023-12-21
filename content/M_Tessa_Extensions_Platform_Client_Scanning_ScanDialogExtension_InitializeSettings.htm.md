# ScanDialogExtension.InitializeSettings - метод
Вызывается при инициализации настроек для диалога сканирования.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task InitializeSettings(
    	ScanFileDialogSettings settings
    )
VB __Копировать
     Public Overridable Function InitializeSettings ( 
    	settings As ScanFileDialogSettings
    ) As Task
C++ __Копировать
     public:
    virtual Task^ InitializeSettings(
    	ScanFileDialogSettings^ settings
    )
F# __Копировать
     abstract InitializeSettings : 
            settings : ScanFileDialogSettings -> Task 
    override InitializeSettings : 
            settings : ScanFileDialogSettings -> Task 
#### Параметры
settings
[ScanFileDialogSettings](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings.htm)
    Настройки диалога сканирования или диалога редактирования изображений.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IScanDialogExtension.InitializeSettings(ScanFileDialogSettings)](M_Tessa_Extensions_Platform_Client_Scanning_IScanDialogExtension_InitializeSettings.htm)  
##  __См. также
#### Ссылки
[ScanDialogExtension -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanDialogExtension.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
