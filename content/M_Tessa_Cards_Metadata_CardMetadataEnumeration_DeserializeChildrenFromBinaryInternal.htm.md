# CardMetadataEnumeration.DeserializeChildrenFromBinaryInternal - метод
Выполняет десериализацию всех дочерних объектов из байтового потока.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override void DeserializeChildrenFromBinaryInternal(
    	BinaryReader reader
    )
VB __Копировать
     Protected Overrides Sub DeserializeChildrenFromBinaryInternal ( 
    	reader As BinaryReader
    )
C++ __Копировать
     protected:
    virtual void DeserializeChildrenFromBinaryInternal(
    	BinaryReader^ reader
    ) override
F# __Копировать
     abstract DeserializeChildrenFromBinaryInternal : 
            reader : BinaryReader -> unit 
    override DeserializeChildrenFromBinaryInternal : 
            reader : BinaryReader -> unit 
#### Параметры
reader
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader)
    Объект, осуществляющий чтение из байтового потока.
##  __См. также
#### Ссылки
[CardMetadataEnumeration -
](T_Tessa_Cards_Metadata_CardMetadataEnumeration.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
