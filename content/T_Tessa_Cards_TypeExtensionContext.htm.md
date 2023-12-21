# TypeExtensionContext - класс
Контекст выполнения расширения на тип карточки
[CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class TypeExtensionContext : ITypeExtensionContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class TypeExtensionContext
    	Implements ITypeExtensionContext, IExtensionContext
C++ __Копировать
     public ref class TypeExtensionContext sealed : ITypeExtensionContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type TypeExtensionContext = 
        class
            interface ITypeExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TypeExtensionContext
Implements
    [ITypeExtensionContext](T_Tessa_Cards_ITypeExtensionContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[TypeExtensionContext](M_Tessa_Cards_TypeExtensionContext__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[CancellationToken](P_Tessa_Cards_TypeExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[Card](P_Tessa_Cards_TypeExtensionContext_Card.htm)| Объект карточки, файла
или задания, для которого выполняется расширение.  
[CardFile](P_Tessa_Cards_TypeExtensionContext_CardFile.htm)|  Файл, для
которого выполняется расширение, или null, если расширение не связано с
файлом.  
[CardMetadata](P_Tessa_Cards_TypeExtensionContext_CardMetadata.htm)|
Метаинформация по типам карточек, файлов и заданий.  
[CardTask](P_Tessa_Cards_TypeExtensionContext_CardTask.htm)|  Задание, для
которого выполняется расширение, или null, если расширение не связано с
заданием.  
[CardType](P_Tessa_Cards_TypeExtensionContext_CardType.htm)| Тип карточки,
файла или задания, для которого выполняется расширение.  
[Extension](P_Tessa_Cards_TypeExtensionContext_Extension.htm)| Метаинформация
по выполняемому расширению.  
[ExternalContext](P_Tessa_Cards_TypeExtensionContext_ExternalContext.htm)|
Внешний контекст расширения, в рамках которого выполняется расширение на тип
карточки, или null, если такой контекст неизвестен.  
[Info](P_Tessa_Cards_TypeExtensionContext_Info.htm)| Дополнительная
информация, связанная с контекстом.  
[MainCard](P_Tessa_Cards_TypeExtensionContext_MainCard.htm)|  Карточка, в
рамках которой выполняется расширение. Не должно быть равно null.  
[MainCardType](P_Tessa_Cards_TypeExtensionContext_MainCardType.htm)|  Тип
карточки, в рамках которого выполняется расширение. Не должен быть равен null.  
[Settings](P_Tessa_Cards_TypeExtensionContext_Settings.htm)| Настройки
выполняемого расширения.  
[ValidationResult](P_Tessa_Cards_TypeExtensionContext_ValidationResult.htm)|
Результат валидации, связанный с расширениями.  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
