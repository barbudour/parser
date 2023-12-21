# DocLoadExtensionContext - класс
Контекст расширений для потокового ввода.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.DocLoad](N_Tessa_Extensions_Platform_Server_DocLoad.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DocLoadExtensionContext : IDocLoadExtensionContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class DocLoadExtensionContext
    	Implements IDocLoadExtensionContext, IExtensionContext
C++ __Копировать
     public ref class DocLoadExtensionContext sealed : IDocLoadExtensionContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type DocLoadExtensionContext = 
        class
            interface IDocLoadExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DocLoadExtensionContext
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [IDocLoadExtensionContext](T_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadExtensionContext.htm)
##  __Конструкторы
[DocLoadExtensionContext](M_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtensionContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Barcode](P_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtensionContext_Barcode.htm)|
Штрих-код, распознанный на изображении.  
---|---  
[CancellationToken](P_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[CardID](P_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtensionContext_CardID.htm)|
Идентификатор карточки, найденный расширением по штрих-коду, указанному в
контексте. Расширение должно установить идентификатор в этом свойстве.  
[DbScope](P_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtensionContext_DbScope.htm)|
Объект для взаимодействия с базой данных.  
[Document](P_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtensionContext_Document.htm)|
Документ, прикрепляемый к карточке.  
[InputFilePath](P_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtensionContext_InputFilePath.htm)|
Файл, полученный на распознавание.  
[Settings](P_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtensionContext_Settings.htm)|
Настройки модуля потокового сканирования.  
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
[Tessa.Extensions.Platform.Server.DocLoad - пространство
имён](N_Tessa_Extensions_Platform_Server_DocLoad.htm)
