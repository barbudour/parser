# CardTypeControl.DeserializeFromBinaryInternal - метод
Выполняет десериализацию всех полей текущего объекта из байтового потока.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override void DeserializeFromBinaryInternal(
    	BinaryReader reader
    )
VB __Копировать
     Protected Overrides Sub DeserializeFromBinaryInternal ( 
    	reader As BinaryReader
    )
C++ __Копировать
     protected:
    virtual void DeserializeFromBinaryInternal(
    	BinaryReader^ reader
    ) override
F# __Копировать
     abstract DeserializeFromBinaryInternal : 
            reader : BinaryReader -> unit 
    override DeserializeFromBinaryInternal : 
            reader : BinaryReader -> unit 
#### Параметры
reader
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader)
    Объект, осуществляющий чтение из байтового потока.
##  __См. также
#### Ссылки
[CardTypeControl - ](T_Tessa_Cards_CardTypeControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
