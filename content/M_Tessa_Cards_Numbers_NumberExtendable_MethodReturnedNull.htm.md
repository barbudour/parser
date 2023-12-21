# NumberExtendable.MethodReturnedNull - метод
Создаёт и возвращает исключение, которое вызывается в случае, когда
перегруженный виртуальный метод вернул null, хотя он не должен был возвращать
null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected InvalidOperationException MethodReturnedNull(
    	string methodName
    )
VB __Копировать
     Protected Function MethodReturnedNull ( 
    	methodName As String
    ) As InvalidOperationException
C++ __Копировать
     protected:
    InvalidOperationException^ MethodReturnedNull(
    	String^ methodName
    )
F# __Копировать
     member MethodReturnedNull : 
            methodName : string -> InvalidOperationException 
#### Параметры
methodName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя метода.
#### Возвращаемое значение
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)  
Созданное исключение.
##  __См. также
#### Ссылки
[NumberExtendable - ](T_Tessa_Cards_Numbers_NumberExtendable.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
