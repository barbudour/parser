# CardMetadataSection.SerializeChildrenToBinaryInternal - метод
Выполняет сериализацию всех дочерних объектов в байтовый поток.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override void SerializeChildrenToBinaryInternal(
    	BinaryWriter writer
    )
VB __Копировать
     Protected Overrides Sub SerializeChildrenToBinaryInternal ( 
    	writer As BinaryWriter
    )
C++ __Копировать
     protected:
    virtual void SerializeChildrenToBinaryInternal(
    	BinaryWriter^ writer
    ) override
F# __Копировать
     abstract SerializeChildrenToBinaryInternal : 
            writer : BinaryWriter -> unit 
    override SerializeChildrenToBinaryInternal : 
            writer : BinaryWriter -> unit 
#### Параметры
writer
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter)
    Объект, осуществляющий запись в байтовый поток.
##  __См. также
#### Ссылки
[CardMetadataSection - ](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
