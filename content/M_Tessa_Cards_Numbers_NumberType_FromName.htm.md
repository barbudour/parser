# NumberType.FromName - метод
Возвращает тип по уникальному имени, полученному посредством метода
[Tessa.Platform.RegistryItem{TItem}.ToName].
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static NumberType FromName(
    	string name
    )
VB __Копировать
     Public Shared Function FromName ( 
    	name As String
    ) As NumberType
C++ __Копировать
     public:
    static NumberType^ FromName(
    	String^ name
    )
F# __Копировать
     static member FromName : 
            name : string -> NumberType 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Уникальное имя, по которому можно восстановить тип.
#### Возвращаемое значение
[NumberType](T_Tessa_Cards_Numbers_NumberType.htm)  
Тип, восстановленный по заданному уникальному имени.
##  __См. также
#### Ссылки
[NumberType - ](T_Tessa_Cards_Numbers_NumberType.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
