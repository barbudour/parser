# MailFileFactory.Create(String, String, Encoding) - метод
Создаёт файл, который может прикладываться к письму и текстовые данные
которого встроены в структуру объекта [MailFile](T_Tessa_Notices_MailFile.htm)
в кодировке encoding. Рекомендуется использовать только для небольших файлов
(желательно не более 100 Кб).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static MailFile Create(
    	string fileName,
    	string content,
    	Encoding encoding = null
    )
VB __Копировать
     Public Shared Function Create ( 
    	fileName As String,
    	content As String,
    	Optional encoding As Encoding = Nothing
    ) As MailFile
C++ __Копировать
     public:
    static MailFile^ Create(
    	String^ fileName, 
    	String^ content, 
    	Encoding^ encoding = nullptr
    )
F# __Копировать
     static member Create : 
            fileName : string * 
            content : string * 
            ?encoding : Encoding 
    (* Defaults:
            let _encoding = defaultArg encoding null
    *)
    -> MailFile 
#### Параметры
fileName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя прикладываемого файла.
content [String](https://learn.microsoft.com/dotnet/api/system.string)
    Содержимое файла в виде текста. Значение null аналогично пустой строке.
encoding
[Encoding](https://learn.microsoft.com/dotnet/api/system.text.encoding)
(Optional)
    Кодировка текста в файле или null, если используется кодировка [UTF8](https://learn.microsoft.com/dotnet/api/system.text.encoding.utf8#system-text-encoding-utf8).
#### Возвращаемое значение
[MailFile](T_Tessa_Notices_MailFile.htm)  
Файл, приложенный к письму.
##  __См. также
#### Ссылки
[MailFileFactory -
](T_Tessa_Extensions_Default_Shared_Notices_MailFileFactory.htm)
[Create -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Notices_MailFileFactory_Create.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
