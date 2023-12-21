# ClientConditionTypesProvider - класс
Объект, который производит получение информации о типах условий на клиенте.
Получение информации возможно только после окончательного формирования
метаданных со всеми расширениями.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Conditions](N_Tessa_Platform_Conditions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ClientConditionTypesProvider : IConditionTypesProvider
VB __Копировать
     Public NotInheritable Class ClientConditionTypesProvider
    	Implements IConditionTypesProvider
C++ __Копировать
     public ref class ClientConditionTypesProvider sealed : IConditionTypesProvider
F# __Копировать
     [<SealedAttribute>]
    type ClientConditionTypesProvider = 
        class
            interface IConditionTypesProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ClientConditionTypesProvider
Implements
    [IConditionTypesProvider](T_Tessa_Platform_Conditions_IConditionTypesProvider.htm)
##  __Конструкторы
[ClientConditionTypesProvider](M_Tessa_Platform_Conditions_ClientConditionTypesProvider__ctor.htm)|
Инициализирует новый экземпляр класса ClientConditionTypesProvider  
---|---  
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
[GetAllAsync](M_Tessa_Platform_Conditions_ClientConditionTypesProvider_GetAllAsync.htm)|
Метод для получения всех типов условий.  
[GetAsync](M_Tessa_Platform_Conditions_ClientConditionTypesProvider_GetAsync.htm)|
Метод для получения типа условия по его идентификатору.  
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
[Initialize](M_Tessa_Platform_Conditions_ClientConditionTypesProvider_Initialize.htm)|
Производит инициализацию типов условий на клиенте по переданным данным.
Инициализация может быть вызвана только раз.  
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
[Tessa.Platform.Conditions - пространство
имён](N_Tessa_Platform_Conditions.htm)
