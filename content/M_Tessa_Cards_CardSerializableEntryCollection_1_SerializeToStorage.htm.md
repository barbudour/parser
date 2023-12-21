# CardSerializableEntryCollection<T>.SerializeToStorage(Dictionary<String,
Object>, String) - метод
Сериализует объект и его дочерние объекты в заданное хранилище
Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void SerializeToStorage(
    	Dictionary<string, Object> storage,
    	string key
    )
VB __Копировать
     Public Sub SerializeToStorage ( 
    	storage As Dictionary(Of String, Object),
    	key As String
    )
C++ __Копировать
     public:
    void SerializeToStorage(
    	Dictionary<String^, Object^>^ storage, 
    	String^ key
    )
F# __Копировать
     member SerializeToStorage : 
            storage : Dictionary<string, Object> * 
            key : string -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, в которое будут сериализованы данные.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому будут размещены дочерние объекты.
##  __См. также
#### Ссылки
[CardSerializableEntryCollection<T> \-
](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
[SerializeToStorage -
перегрузка](Overload_Tessa_Cards_CardSerializableEntryCollection_1_SerializeToStorage.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
