# LocalFileEntry - конструктор
Инициализирует новый экземпляр объекта
[LocalFileEntry](T_Tessa_Applications_Synchronization_LocalFileEntry.htm).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public LocalFileEntry(
    	string fullPath,
    	byte[] hash,
    	string key = null
    )
VB __Копировать
     Public Sub New ( 
    	fullPath As String,
    	hash As Byte(),
    	Optional key As String = Nothing
    )
C++ __Копировать
     public:
    LocalFileEntry(
    	String^ fullPath, 
    	array<unsigned char>^ hash, 
    	String^ key = nullptr
    )
F# __Копировать
     new : 
            fullPath : string * 
            hash : byte[] * 
            ?key : string 
    (* Defaults:
            let _key = defaultArg key null
    *)
    -> LocalFileEntry
#### Параметры
fullPath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Полный путь к файлу.
hash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
    Хеш файла.
key [String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
    Значение используемое в качестве ключа в [LocalFileEntryCollection](T_Tessa_Applications_Synchronization_LocalFileEntryCollection.htm). Если не задано, то будет вычислено автоматически.
##  __См. также
#### Ссылки
[LocalFileEntry - ](T_Tessa_Applications_Synchronization_LocalFileEntry.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
