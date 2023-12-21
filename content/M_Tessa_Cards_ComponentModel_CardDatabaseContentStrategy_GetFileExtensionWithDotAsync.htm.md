# CardDatabaseContentStrategy.GetFileExtensionWithDotAsync - метод
Возвращает расширение указанного файла с точкой. Возвращает строку ".", если
имя файла не найдено.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<string> GetFileExtensionWithDotAsync(
    	DbManager db,
    	IQueryBuilderFactory builderFactory,
    	Guid versionRowID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function GetFileExtensionWithDotAsync ( 
    	db As DbManager,
    	builderFactory As IQueryBuilderFactory,
    	versionRowID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of String)
C++ __Копировать
     protected:
    virtual Task<String^>^ GetFileExtensionWithDotAsync(
    	DbManager^ db, 
    	IQueryBuilderFactory^ builderFactory, 
    	Guid versionRowID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetFileExtensionWithDotAsync : 
            db : DbManager * 
            builderFactory : IQueryBuilderFactory * 
            versionRowID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
    override GetFileExtensionWithDotAsync : 
            db : DbManager * 
            builderFactory : IQueryBuilderFactory * 
            versionRowID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
#### Параметры
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, предоставляющий доступ к базе данных.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
    Объект для генерации текста запросов.
versionRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Версия файла, для которой возвращается расширение в соответствии с именем, которое должно быть в базе данных.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Расширение указанного файла с точкой. Возвращает строку ".", если имя файла не
найдено.
## __См. также
#### Ссылки
[CardDatabaseContentStrategy -
](T_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
