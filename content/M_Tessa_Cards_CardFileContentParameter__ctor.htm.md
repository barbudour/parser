# CardFileContentParameter - конструктор
Создаёт экземпляр класса с указанием информации о файле и его контенте.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileContentParameter(
    	Card card,
    	StringDictionaryStorage<CardRow> sectionRows,
    	CardFile file,
    	Guid fileID,
    	long size,
    	int fileCount,
    	int fileIndex,
    	Stream content,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	card As Card,
    	sectionRows As StringDictionaryStorage(Of CardRow),
    	file As CardFile,
    	fileID As Guid,
    	size As Long,
    	fileCount As Integer,
    	fileIndex As Integer,
    	content As Stream,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardFileContentParameter(
    	Card^ card, 
    	StringDictionaryStorage<CardRow^>^ sectionRows, 
    	CardFile^ file, 
    	Guid fileID, 
    	long long size, 
    	int fileCount, 
    	int fileIndex, 
    	Stream^ content, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            card : Card * 
            sectionRows : StringDictionaryStorage<CardRow> * 
            file : CardFile * 
            fileID : Guid * 
            size : int64 * 
            fileCount : int * 
            fileIndex : int * 
            content : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardFileContentParameter
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой предоставляется информация о файле и его контенте.
sectionRows
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>
    Пустые строки коллекционных и древовидных секций.
file [CardFile](T_Tessa_Cards_CardFile.htm)
    Информация о файле из карточки.
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла.
size [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
    Размер контента файла в байтах.
fileCount [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Количество приложенных к карточке файлов.
fileIndex [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Отсчитываемый от нуля порядковый номер файла.
content [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
    Контент файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[CardFileContentParameter - ](T_Tessa_Cards_CardFileContentParameter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
