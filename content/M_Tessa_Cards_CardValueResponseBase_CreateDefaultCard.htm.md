# CardValueResponseBase.CreateDefaultCard - метод
Создаёт объект карточки по заданному хранилищу. Может автоматически изменить
тип карточки InstanceType после создания.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Card CreateDefaultCard(
    	Dictionary<string, Object> storage
    )
VB __Копировать
     Protected Overridable Function CreateDefaultCard ( 
    	storage As Dictionary(Of String, Object)
    ) As Card
C++ __Копировать
     protected:
    virtual Card^ CreateDefaultCard(
    	Dictionary<String^, Object^>^ storage
    )
F# __Копировать
     abstract CreateDefaultCard : 
            storage : Dictionary<string, Object> -> Card 
    override CreateDefaultCard : 
            storage : Dictionary<string, Object> -> Card 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище карточки.
#### Возвращаемое значение
[Card](T_Tessa_Cards_Card.htm)  
Созданный объект.
##  __См. также
#### Ссылки
[CardValueResponseBase - ](T_Tessa_Cards_CardValueResponseBase.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
