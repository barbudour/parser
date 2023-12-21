# NumberBuilder.TryGet<T> \- метод
Возвращает значение поля в строковой секции карточки или значение по умолчанию
для типа T, если поле или секция отсутствуют.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static T TryGet<T>(
    	Card card,
    	string sectionName,
    	string fieldName
    )
VB __Копировать
     Protected Shared Function TryGet(Of T) ( 
    	card As Card,
    	sectionName As String,
    	fieldName As String
    ) As T
C++ __Копировать
     protected:
    generic<typename T>
    static T TryGet(
    	Card^ card, 
    	String^ sectionName, 
    	String^ fieldName
    )
F# __Копировать
     static member TryGet : 
            card : Card * 
            sectionName : string * 
            fieldName : string -> 'T 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Строковая секция карточки.
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя поля в секции sectionName.
#### Параметры типа
T
    Тип поля.
#### Возвращаемое значение
T  
Значение поля в строковой секции карточки или значение по умолчанию для типа
T, если поле или секция отсутствуют.
## __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
