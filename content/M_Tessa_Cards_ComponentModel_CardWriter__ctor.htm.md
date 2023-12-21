# CardWriter - конструктор
Создаёт экземпляр класса, обеспечивающего запись данных в заданный поток
карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardWriter(
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
    CardWriter(
    	Stream^ cardStream, 
    	SerializableObjectFormat format
    )
F# __Копировать
     new : 
            cardStream : Stream * 
            format : SerializableObjectFormat -> CardWriter
#### Параметры
cardStream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
    Поток карточки, запись данных в который требуется обеспечить.
format
[SerializableObjectFormat](T_Tessa_Platform_IO_SerializableObjectFormat.htm)
    Формат сериализации.
##  __См. также
#### Ссылки
[CardWriter - ](T_Tessa_Cards_ComponentModel_CardWriter.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
