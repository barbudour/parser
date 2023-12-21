# CardStorageCompressor.Decompress - метод
Выполняет распаковку данных, располагающихся в хранилище storage по ключу
targetKey. Данные должны быть запакованы этим же или совместимым объектом
[Tessa.Platform.Storage.IStorageCompressor].
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void Decompress(
    	IDictionary<string, Object> storage,
    	string targetKey
    )
VB __Копировать
     Public Sub Decompress ( 
    	storage As IDictionary(Of String, Object),
    	targetKey As String
    )
C++ __Копировать
     public:
    virtual void Decompress(
    	IDictionary<String^, Object^>^ storage, 
    	String^ targetKey
    ) sealed
F# __Копировать
     abstract Decompress : 
            storage : IDictionary<string, Object> * 
            targetKey : string -> unit 
    override Decompress : 
            storage : IDictionary<string, Object> * 
            targetKey : string -> unit 
#### Параметры
storage
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, в котором располагаются данные, подлежащие распаковке.
targetKey [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому данные, подлежащие распаковке, располагаются в заданном хранилище. Если параметр равен null, то подразумевается, что распаковано должно быть само хранилище, а не один из его вложенных объектов. 
#### Реализации
[IStorageCompressor.Decompress(IDictionary<String, Object>,
String)](M_Tessa_Platform_Storage_IStorageCompressor_Decompress.htm)  
##  __См. также
#### Ссылки
[CardStorageCompressor - ](T_Tessa_Cards_CardStorageCompressor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
