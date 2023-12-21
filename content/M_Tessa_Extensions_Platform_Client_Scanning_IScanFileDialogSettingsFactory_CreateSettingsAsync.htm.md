# IScanFileDialogSettingsFactory.CreateSettingsAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     Task<ScanFileDialogSettings> CreateSettingsAsync(
    	IFileExtensionContextBase context,
    	string menuActionName = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CreateSettingsAsync ( 
    	context As IFileExtensionContextBase,
    	Optional menuActionName As String = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ScanFileDialogSettings)
C++ __Копировать
    Task<ScanFileDialogSettings^>^ CreateSettingsAsync(
    	IFileExtensionContextBase^ context, 
    	String^ menuActionName = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CreateSettingsAsync : 
            context : IFileExtensionContextBase * 
            ?menuActionName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _menuActionName = defaultArg menuActionName null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ScanFileDialogSettings> 
#### Параметры
context
[IFileExtensionContextBase](T_Tessa_UI_Files_IFileExtensionContextBase.htm)
menuActionName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ScanFileDialogSettings](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings.htm)>
##  __См. также
#### Ссылки
[IScanFileDialogSettingsFactory -
](T_Tessa_Extensions_Platform_Client_Scanning_IScanFileDialogSettingsFactory.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
