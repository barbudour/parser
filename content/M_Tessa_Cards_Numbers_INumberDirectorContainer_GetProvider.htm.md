# INumberDirectorContainer.GetProvider - метод
Возвращает объект, предоставляющий доступ к объектам API номеров для заданного
типа карточки или для карточек всех типов по умолчанию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     INumberDirectorProvider GetProvider(
    	Guid? typeID = null
    )
VB __Копировать
     Function GetProvider ( 
    	Optional typeID As Guid? = Nothing
    ) As INumberDirectorProvider
C++ __Копировать
    INumberDirectorProvider^ GetProvider(
    	Nullable<Guid> typeID = nullptr
    )
F# __Копировать
     abstract GetProvider : 
            ?typeID : Nullable<Guid> 
    (* Defaults:
            let _typeID = defaultArg typeID null
    *)
    -> INumberDirectorProvider 
#### Параметры
typeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Тип карточки, для которого возвращается объект, предоставляющий доступ к объектам API номеров, или null, если возвращает объект, предоставляющий доступ к объектами API номеров по умолчанию для всех типов карточек. 
#### Возвращаемое значение
[INumberDirectorProvider](T_Tessa_Cards_Numbers_INumberDirectorProvider.htm)  
Объект, предоставляющий доступ к объектам API номеров.
##  __См. также
#### Ссылки
[INumberDirectorContainer -
](T_Tessa_Cards_Numbers_INumberDirectorContainer.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
