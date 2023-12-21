# CardStorageCompressor.Compress - метод
Выполняет упаковку данных, располагающихся в хранилище storage по ключу
targetKey.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void Compress(
    	IDictionary<string, Object> storage,
    	string targetKey
    )
VB __Копировать
     Public Sub Compress ( 
    	storage As IDictionary(Of String, Object),
    	targetKey As String
    )
C++ __Копировать
     public:
    virtual void Compress(
    	IDictionary<String^, Object^>^ storage, 
    	String^ targetKey
    ) sealed
F# __Копировать
     abstract Compress : 
            storage : IDictionary<string, Object> * 
            targetKey : string -> unit 
    override Compress : 
            storage : IDictionary<string, Object> * 
            targetKey : string -> unit 
#### Параметры
storage
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, в котором располагаются данные, подлежащие упаковке.
targetKey [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому данные, подлежащие упаковке, располагаются в заданном хранилище. Если параметр равен null, то подразумевается, что упаковано должно быть само хранилище, а не один из его вложенных объектов. 
#### Реализации
[IStorageCompressor.Compress(IDictionary<String, Object>,
String)](M_Tessa_Platform_Storage_IStorageCompressor_Compress.htm)  
##  __Заметки
Упакованные данные могут быть полностью или частично недоступны для обработки
через декораторы.
##  __См. также
#### Ссылки
[CardStorageCompressor - ](T_Tessa_Cards_CardStorageCompressor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
