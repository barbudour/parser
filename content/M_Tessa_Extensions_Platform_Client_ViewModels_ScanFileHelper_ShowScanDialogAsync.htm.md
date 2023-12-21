# ScanFileHelper.ShowScanDialogAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.ViewModels](N_Tessa_Extensions_Platform_Client_ViewModels.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task ShowScanDialogAsync(
    	ScanFileDialogSettings settings,
    	ICollection<ITempFile> initialFiles = null
    )
VB __Копировать
     Public Shared Function ShowScanDialogAsync ( 
    	settings As ScanFileDialogSettings,
    	Optional initialFiles As ICollection(Of ITempFile) = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ ShowScanDialogAsync(
    	ScanFileDialogSettings^ settings, 
    	ICollection<ITempFile^>^ initialFiles = nullptr
    )
F# __Копировать
     static member ShowScanDialogAsync : 
            settings : ScanFileDialogSettings * 
            ?initialFiles : ICollection<ITempFile> 
    (* Defaults:
            let _initialFiles = defaultArg initialFiles null
    *)
    -> Task 
#### Параметры
settings
[ScanFileDialogSettings](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings.htm)
initialFiles
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[ITempFile](T_Tessa_Platform_IO_ITempFile.htm)>
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[ScanFileHelper -
](T_Tessa_Extensions_Platform_Client_ViewModels_ScanFileHelper.htm)
[Tessa.Extensions.Platform.Client.ViewModels - пространство
имён](N_Tessa_Extensions_Platform_Client_ViewModels.htm)
