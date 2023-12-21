# CreateFileContainerFuncAsync - делегат
Создаёт контейнер файлов для заданного источника файлов, обеспечивающего
взаимодействие созданных с его помощью файлов с внешней подсистемой.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate ValueTask<IFileContainer> CreateFileContainerFuncAsync(
    	IFileSource source,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function CreateFileContainerFuncAsync ( 
    	source As IFileSource,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IFileContainer)
C++ __Копировать
     public delegate ValueTask<IFileContainer^> CreateFileContainerFuncAsync(
    	IFileSource^ source, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type CreateFileContainerFuncAsync = 
        delegate of 
            source : IFileSource * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileContainer>
#### Параметры
source [IFileSource](T_Tessa_Files_IFileSource.htm)
     Источник файлов по умолчанию, обеспечивающий взаимодействие созданных с его помощью файлов с внешней подсистемой. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IFileContainer](T_Tessa_Files_IFileContainer.htm)>  
Созданный контейнер файлов.
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
