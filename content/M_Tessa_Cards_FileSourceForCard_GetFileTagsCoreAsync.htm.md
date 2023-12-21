# FileSourceForCard.GetFileTagsCoreAsync - метод
Возвращает список тегов для файла. Обычно используется при добавлении файла на
клиенте. При сохранении карточки с файлами необходимые теги файлов добавляются
автоматически, независимо от результата метода. Возвращённое значение не равно
null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<List<IFileTag>> GetFileTagsCoreAsync(
    	string filePath,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function GetFileTagsCoreAsync ( 
    	filePath As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of List(Of IFileTag))
C++ __Копировать
     protected:
    virtual ValueTask<List<IFileTag^>^> GetFileTagsCoreAsync(
    	String^ filePath, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract GetFileTagsCoreAsync : 
            filePath : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<List<IFileTag>> 
    override GetFileTagsCoreAsync : 
            filePath : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<List<IFileTag>> 
#### Параметры
filePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к файлу на диске, по которому требуется определить список тегов.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>>  
Список тегов для файла. Возвращённое значение не равно null.
## __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
