# ErrorDescriptionSerializer - класс
Объект, управляющий сериализацией описаний ошибок
[IErrorDescription](T_Tessa_Platform_Runtime_IErrorDescription.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ErrorDescriptionSerializer : IErrorDescriptionSerializer
VB __Копировать
     Public NotInheritable Class ErrorDescriptionSerializer
    	Implements IErrorDescriptionSerializer
C++ __Копировать
     public ref class ErrorDescriptionSerializer sealed : IErrorDescriptionSerializer
F# __Копировать
     [<SealedAttribute>]
    type ErrorDescriptionSerializer = 
        class
            interface IErrorDescriptionSerializer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ErrorDescriptionSerializer
Implements
    [IErrorDescriptionSerializer](T_Tessa_Platform_Runtime_IErrorDescriptionSerializer.htm)
##  __Конструкторы
[ErrorDescriptionSerializer](M_Tessa_Platform_Runtime_ErrorDescriptionSerializer__ctor.htm)|
Инициализирует новый экземпляр класса ErrorDescriptionSerializer  
---|---  
##  __Методы
[Deserialize](M_Tessa_Platform_Runtime_ErrorDescriptionSerializer_Deserialize.htm)|
Десериализует объект с описанием ошибки из хеш-таблицы, которая могла быть
прочитана из строки таблицы с историей действий.  
---|---  
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
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Serialize](M_Tessa_Platform_Runtime_ErrorDescriptionSerializer_Serialize.htm)|
Сериализует объект с описанием ошибки в форме хеш-таблицы, которая может быть
записана в строку таблицы с историей действий.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[CategoryKey](F_Tessa_Platform_Runtime_ErrorDescriptionSerializer_CategoryKey.htm)|
Ключ сериализации для свойства
[Category](P_Tessa_Platform_Runtime_IErrorDescription_Category.htm).  
---|---  
[InfoKey](F_Tessa_Platform_Runtime_ErrorDescriptionSerializer_InfoKey.htm)|
Ключ сериализации для свойства
[Info](P_Tessa_Platform_Runtime_IErrorDescription_Info.htm).  
[TextKey](F_Tessa_Platform_Runtime_ErrorDescriptionSerializer_TextKey.htm)|
Ключ сериализации для свойства
[Text](P_Tessa_Platform_Runtime_IErrorDescription_Text.htm).  
[ValidationResultKey](F_Tessa_Platform_Runtime_ErrorDescriptionSerializer_ValidationResultKey.htm)|
Ключ сериализации для свойства
[ValidationResult](P_Tessa_Platform_Runtime_IErrorDescription_ValidationResult.htm).  
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
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
