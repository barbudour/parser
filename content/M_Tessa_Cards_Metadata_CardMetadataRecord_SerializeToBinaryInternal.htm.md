# CardMetadataRecord.SerializeToBinaryInternal - метод
Выполняет сериализацию текущего объекта в байтовый поток.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override void SerializeToBinaryInternal(
    	BinaryWriter writer
    )
VB __Копировать
     Protected Overrides Sub SerializeToBinaryInternal ( 
    	writer As BinaryWriter
    )
C++ __Копировать
     protected:
    virtual void SerializeToBinaryInternal(
    	BinaryWriter^ writer
    ) override
F# __Копировать
     abstract SerializeToBinaryInternal : 
            writer : BinaryWriter -> unit 
    override SerializeToBinaryInternal : 
            writer : BinaryWriter -> unit 
#### Параметры
writer
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter)
    Объект, осуществляющий запись в байтовый поток.
##  __См. также
#### Ссылки
[CardMetadataRecord - ](T_Tessa_Cards_Metadata_CardMetadataRecord.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
