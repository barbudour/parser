# CardReader - конструктор
Создаёт экземпляр класса с указанием потока карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardReader(
    	Stream cardStream,
    	SerializableObjectFormat format
    )
VB __Копировать
     Public Sub New ( 
    	cardStream As Stream,
    	format As SerializableObjectFormat
    )
C++ __Копировать
     public:
    CardReader(
    	Stream^ cardStream, 
    	SerializableObjectFormat format
    )
F# __Копировать
     new : 
            cardStream : Stream * 
            format : SerializableObjectFormat -> CardReader
#### Параметры
cardStream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
    Поток карточки, чтение данных из которого обеспечивает создаваемый объект.
format
[SerializableObjectFormat](T_Tessa_Platform_IO_SerializableObjectFormat.htm)
    Формат сериализации.
##  __См. также
#### Ссылки
[CardReader - ](T_Tessa_Cards_ComponentModel_CardReader.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
