# CardTypeBlock.DeserializeChildrenFromBinaryInternal - метод
Выполняет десериализацию всех дочерних объектов из байтового потока.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
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
[CardTypeBlock - ](T_Tessa_Cards_CardTypeBlock.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
