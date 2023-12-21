# CardSerializableEntryCollection<T>.DeserializeFromStorage(Dictionary<String,
Object>, String) - метод
Десериализует объект и его дочерние объекты из заданного хранилища
Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void DeserializeFromStorage(
    	Dictionary<string, Object> storage,
    	string key
    )
VB __Копировать
     Public Sub DeserializeFromStorage ( 
    	storage As Dictionary(Of String, Object),
    	key As String
    )
C++ __Копировать
     public:
    void DeserializeFromStorage(
    	Dictionary<String^, Object^>^ storage, 
    	String^ key
    )
F# __Копировать
     member DeserializeFromStorage : 
            storage : Dictionary<string, Object> * 
            key : string -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, в котором размещены сериализованные данные.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому размещены сериализованные данные в хранилище.
##  __См. также
#### Ссылки
[CardSerializableEntryCollection<T> \-
](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
[DeserializeFromStorage -
перегрузка](Overload_Tessa_Cards_CardSerializableEntryCollection_1_DeserializeFromStorage.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
