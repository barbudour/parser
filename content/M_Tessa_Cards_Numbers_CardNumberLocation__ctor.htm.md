# CardNumberLocation - конструктор
Создаёт экземпляр класса с указанием значений его свойств. Сразу после
создания класс считается защищённым от изменений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardNumberLocation(
    	string section,
    	string numberField,
    	string fullNumberField,
    	string sequenceNameField,
    	INumberLocationManager manager
    )
VB __Копировать
     Public Sub New ( 
    	section As String,
    	numberField As String,
    	fullNumberField As String,
    	sequenceNameField As String,
    	manager As INumberLocationManager
    )
C++ __Копировать
     public:
    CardNumberLocation(
    	String^ section, 
    	String^ numberField, 
    	String^ fullNumberField, 
    	String^ sequenceNameField, 
    	INumberLocationManager^ manager
    )
F# __Копировать
     new : 
            section : string * 
            numberField : string * 
            fullNumberField : string * 
            sequenceNameField : string * 
            manager : INumberLocationManager -> CardNumberLocation
#### Параметры
section [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя секции, содержащей поля с номером. Не может быть равно null. 
numberField [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля с числовым представлением номера. Не может быть равно null. 
fullNumberField [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля со строковым представлением номера. Не может быть равно null. 
sequenceNameField
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля с названием последовательности, из которой был выделен номер. Не может быть равно null. 
manager
[INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm)
     Объект, определяющий поведение номера. Не может быть равен null. 
## __См. также
#### Ссылки
[CardNumberLocation - ](T_Tessa_Cards_Numbers_CardNumberLocation.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
