# CardCacheEventArgs.Serialize - метод
Сериализует объект в бинарной форме.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override void Serialize(
    	BinaryWriter writer
    )
VB __Копировать
     Public Overrides Sub Serialize ( 
    	writer As BinaryWriter
    )
C++ __Копировать
     public:
    virtual void Serialize(
    	BinaryWriter^ writer
    ) override
F# __Копировать
     abstract Serialize : 
            writer : BinaryWriter -> unit 
    override Serialize : 
            writer : BinaryWriter -> unit 
#### Параметры
writer
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter)
    Объект, выполняющий запись в поток в бинарной формы.
#### Реализации
[IBinarySerializable.Serialize(BinaryWriter)](M_Tessa_Platform_IBinarySerializable_Serialize.htm)  
##  __См. также
#### Ссылки
[CardCacheEventArgs - ](T_Tessa_Cards_Caching_CardCacheEventArgs.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
