# CardFieldChangedEventArgs - конструктор
Создаёт экземпляр класса с указанием информации о том, какое поле карточки
было изменено.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFieldChangedEventArgs(
    	string fieldName,
    	Func<Object> getFieldValueFunc
    )
VB __Копировать
     Public Sub New ( 
    	fieldName As String,
    	getFieldValueFunc As Func(Of Object)
    )
C++ __Копировать
     public:
    CardFieldChangedEventArgs(
    	String^ fieldName, 
    	Func<Object^>^ getFieldValueFunc
    )
F# __Копировать
     new : 
            fieldName : string * 
            getFieldValueFunc : Func<Object> -> CardFieldChangedEventArgs
#### Параметры
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля, которое изменилось в строковой секции или в строке коллекционной или древовидной секции. 
getFieldValueFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Функция, возвращающая значение поля, которое изменилось в строковой секции или в строке коллекционной или древовидной секции. 
## __См. также
#### Ссылки
[CardFieldChangedEventArgs - ](T_Tessa_Cards_CardFieldChangedEventArgs.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
