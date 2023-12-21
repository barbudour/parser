# CardAnyFileTypePolicy - класс
Политика, определяющая допустимость любого имени типа файла для выполнения
методов расширения. Может быть использована для замещения другой политики
[ICardFileTypePolicy](T_Tessa_Cards_Extensions_ICardFileTypePolicy.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardAnyFileTypePolicy : ICardFileTypePolicy, 
    	IExtensionPolicy
VB __Копировать
     Public NotInheritable Class CardAnyFileTypePolicy
    	Implements ICardFileTypePolicy, IExtensionPolicy
C++ __Копировать
     public ref class CardAnyFileTypePolicy sealed : ICardFileTypePolicy, 
    	IExtensionPolicy
F# __Копировать
     [<SealedAttribute>]
    type CardAnyFileTypePolicy = 
        class
            interface ICardFileTypePolicy
            interface IExtensionPolicy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardAnyFileTypePolicy
Implements
    [ICardFileTypePolicy](T_Tessa_Cards_Extensions_ICardFileTypePolicy.htm), [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
##  __Заметки
Для использования этой политики требуется зарегистрировать политику
[IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm).
## __Конструкторы
[CardAnyFileTypePolicy](M_Tessa_Cards_Extensions_CardAnyFileTypePolicy__ctor.htm)|
Инициализирует новый экземпляр класса CardAnyFileTypePolicy  
---|---  
##  __Свойства
[Instance](P_Tessa_Cards_Extensions_CardAnyFileTypePolicy_Instance.htm)|
Экземпляр класса.  
---|---  
[IsAllowAny](P_Tessa_Cards_Extensions_CardAnyFileTypePolicy_IsAllowAny.htm)|
Признак того, что политика разрешает любые типы файлов, в том числе
неизвестные на момент фильтрации.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsAllowed(CardType)](M_Tessa_Cards_Extensions_CardAnyFileTypePolicy_IsAllowed_1.htm)|
Возвращает признак того, что выполнение методов расширения допустимо для
заданного типа файла.  
[IsAllowed(String)](M_Tessa_Cards_Extensions_CardAnyFileTypePolicy_IsAllowed.htm)|
Возвращает признак того, что выполнение методов расширения допустимо для типа
файла с заданным именем.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
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
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
