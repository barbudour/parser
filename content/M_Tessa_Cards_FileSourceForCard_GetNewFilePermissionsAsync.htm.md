# FileSourceForCard.GetNewFilePermissionsAsync - метод
Получает разрешения для создаваемого файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override ValueTask<IFilePermissions> GetNewFilePermissionsAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overrides Function GetNewFilePermissionsAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IFilePermissions)
C++ __Копировать
     public:
    virtual ValueTask<IFilePermissions^> GetNewFilePermissionsAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract GetNewFilePermissionsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFilePermissions> 
    override GetNewFilePermissionsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFilePermissions> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IFilePermissions](T_Tessa_Files_IFilePermissions.htm)>  
Разрешения для создаваемого файла.
#### Реализации
[IFileSource.GetNewFilePermissionsAsync(CancellationToken)](M_Tessa_Files_IFileSource_GetNewFilePermissionsAsync.htm)  
##  __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
