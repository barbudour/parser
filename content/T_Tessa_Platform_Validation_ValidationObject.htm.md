# ValidationObject - класс
Объект, поддерживающий валидацию свойств.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public abstract class ValidationObject : IValidationObject, 
    	IValidatable
VB __Копировать
    <SerializableAttribute>
    Public MustInherit Class ValidationObject
    	Implements IValidationObject, IValidatable
C++ __Копировать
    [SerializableAttribute]
    public ref class ValidationObject abstract : IValidationObject, 
    	IValidatable
F# __Копировать
     [<AbstractClassAttribute>]
    [<SerializableAttribute>]
    type ValidationObject = 
        class
            interface IValidationObject
            interface IValidatable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ValidationObject
Derived
[Tessa.Cards.CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Platform.Storage.DictionaryStorage<TKey,
TValue>](T_Tessa_Platform_Storage_DictionaryStorage_2.htm)
[Tessa.Platform.Storage.ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm)
[Tessa.Views.Metadata.ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm)
Implements
    [IValidatable](T_Tessa_Platform_Validation_IValidatable.htm), [IValidationObject](T_Tessa_Platform_Validation_IValidationObject.htm)
##  __Конструкторы
[ValidationObject](M_Tessa_Platform_Validation_ValidationObject__ctor.htm)|
Инициализирует новый экземпляр класса ValidationObject  
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
[GetFieldName<T>](M_Tessa_Platform_Validation_ValidationObject_GetFieldName__1.htm)|
Возвращает имя поля или свойства, заданного выражением вида () =>
this.FieldName.  
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
[GetValidationName](M_Tessa_Platform_Validation_ValidationObject_GetValidationName.htm)|
Возвращает строку, определяющую имя объекта, или null, если имя объекта ещё
неизвестно или объект не содержит имени.  
[IsValid](M_Tessa_Platform_Validation_ValidationObject_IsValid.htm)| Выполняет
проверку объекта на валидность и возвращает признак того, что объект является
валидным.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Validate()](M_Tessa_Platform_Validation_ValidationObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
[ValidateInternal](M_Tessa_Platform_Validation_ValidationObject_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
##  __Поля
[PropertyIsEmpty](F_Tessa_Platform_Validation_ValidationObject_PropertyIsEmpty.htm)|
Ключ сообщения валидации о том, что у заданного свойства пустое значение.  
---|---  
[PropertyIsInvalid](F_Tessa_Platform_Validation_ValidationObject_PropertyIsInvalid.htm)|
Ключ сообщения валидации о том, что у заданного свойства некорректное
значение.  
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
[Validate](M_Tessa_Platform_Validation_ValidationExtensions_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Validation - пространство
имён](N_Tessa_Platform_Validation.htm)
