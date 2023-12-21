# NumberQueueEventType.FromGuid - метод
Возвращает тип по уникальному идентификатору, полученному посредством метода
[Tessa.Platform.RegistryItem{TItem}.ToGuid].
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static NumberQueueEventType FromGuid(
    	Guid guid
    )
VB __Копировать
     Public Shared Function FromGuid ( 
    	guid As Guid
    ) As NumberQueueEventType
C++ __Копировать
     public:
    static NumberQueueEventType^ FromGuid(
    	Guid guid
    )
F# __Копировать
     static member FromGuid : 
            guid : Guid -> NumberQueueEventType 
#### Параметры
guid [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Уникальный идентификатор, по которому можно восстановить тип.
#### Возвращаемое значение
[NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm)  
Тип, восстановленный по заданному уникальному идентификатору.
##  __См. также
#### Ссылки
[NumberQueueEventType - ](T_Tessa_Cards_Numbers_NumberQueueEventType.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
