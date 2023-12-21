# CardCacheEventArgs.Deserialize - метод
Десериализует объект из бинарной формы.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override void Deserialize(
    	BinaryReader reader
    )
VB __Копировать
     Public Overrides Sub Deserialize ( 
    	reader As BinaryReader
    )
C++ __Копировать
     public:
    virtual void Deserialize(
    	BinaryReader^ reader
    ) override
F# __Копировать
     abstract Deserialize : 
            reader : BinaryReader -> unit 
    override Deserialize : 
            reader : BinaryReader -> unit 
#### Параметры
reader
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader)
    Объект, выполняющий чтение из потока в бинарной форме.
#### Реализации
[IBinarySerializable.Deserialize(BinaryReader)](M_Tessa_Platform_IBinarySerializable_Deserialize.htm)  
##  __См. также
#### Ссылки
[CardCacheEventArgs - ](T_Tessa_Cards_Caching_CardCacheEventArgs.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
