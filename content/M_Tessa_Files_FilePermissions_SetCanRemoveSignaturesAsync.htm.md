# FilePermissions.SetCanRemoveSignaturesAsync - метод
Устанавливает признак того, что пользователь может удалить подписи для любой
версии файла. Как правило, такое действие доступно только администратору.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SetCanRemoveSignaturesAsync(
    	bool value,
    	Func<Action, CancellationToken, Task> executePropertyChangedAsync = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SetCanRemoveSignaturesAsync ( 
    	value As Boolean,
    	Optional executePropertyChangedAsync As Func(Of Action, CancellationToken, Task) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ SetCanRemoveSignaturesAsync(
    	bool value, 
    	Func<Action^, CancellationToken, Task^>^ executePropertyChangedAsync = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SetCanRemoveSignaturesAsync : 
            value : bool * 
            ?executePropertyChangedAsync : Func<Action, CancellationToken, Task> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _executePropertyChangedAsync = defaultArg executePropertyChangedAsync null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override SetCanRemoveSignaturesAsync : 
            value : bool * 
            ?executePropertyChangedAsync : Func<Action, CancellationToken, Task> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _executePropertyChangedAsync = defaultArg executePropertyChangedAsync null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Устанавливаемый признак того, что пользователь может удалить подписи для любой версии файла. Как правило, такое действие доступно только администратору. 
executePropertyChangedAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Action](https://learn.microsoft.com/dotnet/api/system.action),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
(Optional)
     Метод, выполняющий изменение свойства (текущий метод может быть вызван из другого потока, тогда этот метод "пробросит" выполнение в поток UI). Если параметр равен null, то изменение свойства выполняется в текущем потоке. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IFilePermissions.SetCanRemoveSignaturesAsync(Boolean, Func<Action,
CancellationToken, Task>,
CancellationToken)](M_Tessa_Files_IFilePermissions_SetCanRemoveSignaturesAsync.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[FilePermissions - ](T_Tessa_Files_FilePermissions.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
[Tessa.Platform.ObjectSealedException]
