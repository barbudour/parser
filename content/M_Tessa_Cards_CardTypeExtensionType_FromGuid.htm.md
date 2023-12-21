# CardTypeExtensionType.FromGuid - метод
Возвращает тип по уникальному идентификатору, полученному посредством метода
[Tessa.Platform.RegistryItem{TItem}.ToGuid].
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardTypeExtensionType FromGuid(
    	Guid guid
    )
VB __Копировать
     Public Shared Function FromGuid ( 
    	guid As Guid
    ) As CardTypeExtensionType
C++ __Копировать
     public:
    static CardTypeExtensionType^ FromGuid(
    	Guid guid
    )
F# __Копировать
     static member FromGuid : 
            guid : Guid -> CardTypeExtensionType 
#### Параметры
guid [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Уникальный идентификатор, по которому можно восстановить тип.
#### Возвращаемое значение
[CardTypeExtensionType](T_Tessa_Cards_CardTypeExtensionType.htm)  
Тип, восстановленный по заданному уникальному идентификатору.
##  __См. также
#### Ссылки
[CardTypeExtensionType - ](T_Tessa_Cards_CardTypeExtensionType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
