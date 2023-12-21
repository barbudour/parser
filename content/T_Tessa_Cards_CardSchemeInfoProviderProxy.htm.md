# CardSchemeInfoProviderProxy - класс
Объект для получения таблиц из
[ISchemeService](T_Tessa_Scheme_ISchemeService.htm). Является "тонкой"
обёрткой без использования кэширования. Не поддерживает метод
[CreateForCardType(CardType)](M_Tessa_Cards_CardSchemeInfoProviderProxy_CreateForCardType.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardSchemeInfoProviderProxy : ICardSchemeInfoProvider, 
    	IAsyncDisposable
VB __Копировать
     Public NotInheritable Class CardSchemeInfoProviderProxy
    	Implements ICardSchemeInfoProvider, IAsyncDisposable
C++ __Копировать
     public ref class CardSchemeInfoProviderProxy sealed : ICardSchemeInfoProvider, 
    	IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type CardSchemeInfoProviderProxy = 
        class
            interface ICardSchemeInfoProvider
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardSchemeInfoProviderProxy
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm)
##  __Конструкторы
[CardSchemeInfoProviderProxy](M_Tessa_Cards_CardSchemeInfoProviderProxy__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[CreateForCardType](M_Tessa_Cards_CardSchemeInfoProviderProxy_CreateForCardType.htm)|
Создает экземпляр
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm),
содержащий таблицы из основной схемы и виртуальной схемы типа карточки
cardType.  
---|---  
[DisposeAsync](M_Tessa_Cards_CardSchemeInfoProviderProxy_DisposeAsync.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources asynchronously.  
[EnsureCacheResolvedAsync](M_Tessa_Cards_CardSchemeInfoProviderProxy_EnsureCacheResolvedAsync.htm)|
Заполняет внутренний кэш объекта, если он используется.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetTableAsync](M_Tessa_Cards_CardSchemeInfoProviderProxy_GetTableAsync.htm)|
Возвращает таблицу по идентификатору. Выбрасывает исключение, если таблица не
найдена.  
[GetTablesAsync](M_Tessa_Cards_CardSchemeInfoProviderProxy_GetTablesAsync.htm)|
Получает все таблицы, доступные в рамках схемы данных текущего объекта.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateCache](M_Tessa_Cards_CardSchemeInfoProviderProxy_InvalidateCache.htm)|
Сбрасывает кэш в текущем объекте.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetTableAsync](M_Tessa_Cards_CardSchemeInfoProviderProxy_TryGetTableAsync.htm)|
Возвращает таблицу по идентификатору или null, если таблица не найдена.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ValidateAsync](M_Tessa_UI_Cards_CardUIExtensions_ValidateAsync_1.htm)|
Выполняет проверку наличия таблицы с идентификатором tableID в схеме.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[ValidateAsync](M_Tessa_UI_Cards_CardUIExtensions_ValidateAsync.htm)|
Выполняет проверку наличия колонки с идентификатором columnID в таблице с
идентификатором tableID.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
