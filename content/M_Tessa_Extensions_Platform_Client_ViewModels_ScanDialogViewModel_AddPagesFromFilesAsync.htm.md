# ScanDialogViewModel.AddPagesFromFilesAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.ViewModels](N_Tessa_Extensions_Platform_Client_ViewModels.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public Task AddPagesFromFilesAsync(
    	ICollection<ITempFile> imageFiles,
    	bool markIsDirty = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function AddPagesFromFilesAsync ( 
    	imageFiles As ICollection(Of ITempFile),
    	Optional markIsDirty As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ AddPagesFromFilesAsync(
    	ICollection<ITempFile^>^ imageFiles, 
    	bool markIsDirty = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member AddPagesFromFilesAsync : 
            imageFiles : ICollection<ITempFile> * 
            ?markIsDirty : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _markIsDirty = defaultArg markIsDirty false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
imageFiles
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[ITempFile](T_Tessa_Platform_IO_ITempFile.htm)>
markIsDirty [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[ScanDialogViewModel -
](T_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel.htm)
[Tessa.Extensions.Platform.Client.ViewModels - пространство
имён](N_Tessa_Extensions_Platform_Client_ViewModels.htm)
