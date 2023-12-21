# CardFileContentProvider(Guid, String, Encoding) - конструктор
Создаёт экземпляр класса для файлов, контент которых задаётся в виде строки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileContentProvider(
    	Guid fileID,
    	string content,
    	Encoding encoding = null
    )
VB __Копировать
     Public Sub New ( 
    	fileID As Guid,
    	content As String,
    	Optional encoding As Encoding = Nothing
    )
C++ __Копировать
     public:
    CardFileContentProvider(
    	Guid fileID, 
    	String^ content, 
    	Encoding^ encoding = nullptr
    )
F# __Копировать
     new : 
            fileID : Guid * 
            content : string * 
            ?encoding : Encoding 
    (* Defaults:
            let _encoding = defaultArg encoding null
    *)
    -> CardFileContentProvider
#### Параметры
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла.
content [String](https://learn.microsoft.com/dotnet/api/system.string)
    Строка с контентом файла. Значение null аналогично пустой строке.
encoding
[Encoding](https://learn.microsoft.com/dotnet/api/system.text.encoding)
(Optional)
    Кодировка текста в файле или null, если используется кодировка [UTF8](https://learn.microsoft.com/dotnet/api/system.text.encoding.utf8#system-text-encoding-utf8).
##  __См. также
#### Ссылки
[CardFileContentProvider - ](T_Tessa_Cards_CardFileContentProvider.htm)
[CardFileContentProvider -
перегрузка](Overload_Tessa_Cards_CardFileContentProvider__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
