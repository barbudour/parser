# CardFileSource - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileSource(
    	CardFileSourceType type,
    	string name,
    	string path,
    	bool isDatabase,
    	bool useSimpleNamingScheme,
    	string fileExtensions = null,
    	int size = 0,
    	int maxSize = 0
    )
VB __Копировать
     Public Sub New ( 
    	type As CardFileSourceType,
    	name As String,
    	path As String,
    	isDatabase As Boolean,
    	useSimpleNamingScheme As Boolean,
    	Optional fileExtensions As String = Nothing,
    	Optional size As Integer = 0,
    	Optional maxSize As Integer = 0
    )
C++ __Копировать
     public:
    CardFileSource(
    	CardFileSourceType type, 
    	String^ name, 
    	String^ path, 
    	bool isDatabase, 
    	bool useSimpleNamingScheme, 
    	String^ fileExtensions = nullptr, 
    	int size = 0, 
    	int maxSize = 0
    )
F# __Копировать
     new : 
            type : CardFileSourceType * 
            name : string * 
            path : string * 
            isDatabase : bool * 
            useSimpleNamingScheme : bool * 
            ?fileExtensions : string * 
            ?size : int * 
            ?maxSize : int 
    (* Defaults:
            let _fileExtensions = defaultArg fileExtensions null
            let _size = defaultArg size 0
            let _maxSize = defaultArg maxSize 0
    *)
    -> CardFileSource
#### Параметры
type [CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)
    Тип местоположения.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Отображаемое имя местоположения.
path [String](https://learn.microsoft.com/dotnet/api/system.string)
     Путь к местоположению. Соответствует имени строки подключения к БД из конфигурационного файла или полному путь к файловой папке. 
isDatabase [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что местоположение соответствует базе данных, а не файловой папке. 
useSimpleNamingScheme
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что используется упрощённая схема именования папок, где для карточек не создаются дополнительные подпапки. Значение true не рекомендуется, если в системе возможны миллионы карточек с файлами, т.к. это приведёт к миллионам подпапок внутри одной папки в файловой системе. Значение неактуально для файлов в базе данных. 
fileExtensions [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Строка со списком расширений, которые рекомендуется использовать с этим источником файлов. Расширения разделены пробелами и обычно без ведущей точки. Строка может быть равна null. 
size [Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
     Текущий размер занятого места в местоположении. Не заполняется и не используется системой, возможно использование в расширениях. 
maxSize [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
(Optional)
     Максимальный размер занятого места в местоположении. Не заполняется и не используется системой, возможно использование в расширениях. 
## __См. также
#### Ссылки
[CardFileSource - ](T_Tessa_Cards_CardFileSource.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
