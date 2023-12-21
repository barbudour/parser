# NumberEventType.FromGuid - метод
Возвращает тип по уникальному идентификатору, полученному посредством метода
[Tessa.Platform.RegistryItem{TItem}.ToGuid].
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static NumberEventType FromGuid(
    	Guid guid
    )
VB __Копировать
     Public Shared Function FromGuid ( 
    	guid As Guid
    ) As NumberEventType
C++ __Копировать
     public:
    static NumberEventType^ FromGuid(
    	Guid guid
    )
F# __Копировать
     static member FromGuid : 
            guid : Guid -> NumberEventType 
#### Параметры
guid [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Уникальный идентификатор, по которому можно восстановить тип.
#### Возвращаемое значение
[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)  
Тип, восстановленный по заданному уникальному идентификатору.
##  __См. также
#### Ссылки
[NumberEventType - ](T_Tessa_Cards_Numbers_NumberEventType.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
