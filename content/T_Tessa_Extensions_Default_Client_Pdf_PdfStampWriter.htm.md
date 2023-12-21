# PdfStampWriter - класс
Объект, выполняющий вывод штампа на странице PDF.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Pdf](N_Tessa_Extensions_Default_Client_Pdf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public class PdfStampWriter
VB __Копировать
     Public Class PdfStampWriter
C++ __Копировать
     public ref class PdfStampWriter
F# __Копировать
     type PdfStampWriter = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PdfStampWriter
##  __Конструкторы
[PdfStampWriter(XFont)](M_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter__ctor.htm)|
Создаёт экземпляр класса с указанием используемого шрифта. Другие свойства
экземпляра устанавливаются значениями по умолчанию.  
---|---  
[PdfStampWriter(String,
Double)](M_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter__ctor_1.htm)|
Создаёт экземпляр класса с указанием параметров используемого шрифта. Другие
свойства экземпляра устанавливаются значениями по умолчанию.  
## __Свойства
[Background](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Background.htm)|
Цвет заливки. По умолчанию используется
[DefaultBackground](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_DefaultBackground.htm).
Если заливка должна отсутствовать, то используйте кисть Transparent.  
---|---  
[Border](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Border.htm)|
Цвет обводки. По умолчанию используется
[DefaultBorder](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_DefaultBorder.htm).  
[DefaultBackground](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_DefaultBackground.htm)|
Цвет
[Background](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Background.htm)
с цветом по умолчанию.  
[DefaultBorder](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_DefaultBorder.htm)|
Цвет [Border](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Border.htm)
с цветом по умолчанию.  
[DefaultForeground](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_DefaultForeground.htm)|
Цвет
[Foreground](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Foreground.htm)
с цветом по умолчанию.  
[Font](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Font.htm)|  Шрифт,
который используется для вывода текста. Установить шрифт можно также
посредством метода [SetFont(String,
Double)](M_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_SetFont.htm).  
[Foreground](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Foreground.htm)|
Цвет текста. По умолчанию используется
[DefaultForeground](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_DefaultForeground.htm).  
[IsEmpty](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_IsEmpty.htm)|
Признак того, что штамп не содержит строк и поэтому не будет выведен.  
[Left](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Left.htm)|
Координата X для левого верхнего угла штампа, измеренная в точках PDF. Не
может быть меньше нуля. По умолчанию равна 20.0.  
[Lines](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Lines.htm)|
Коллекция строк текста, которые выводятся в штампе.  
[Padding](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Padding.htm)|
Отступ от обводки до текста. Не может быть меньше нуля. По умолчанию равен 5
точкам.  
[Top](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Top.htm)|
Координата Y для левого верхнего угла штампа, измеренная в точках PDF. Не
может быть меньше нуля. По умолчанию равна 20.0.  
## __Методы
[AppendLine](M_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_AppendLine.htm)|
Добавляет строку в список строк
[Lines](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Lines.htm).  
---|---  
[Clear](M_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Clear.htm)|
Очищает список строк
[Lines](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Lines.htm).  
[Draw](M_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_Draw.htm)|
Выводим штамп на страницу PDF, для которой задан объект XGraphics. Если штамп
не содержит строк, т.е. свойство
[IsEmpty](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_IsEmpty.htm)
вернуло true, то метод в реализации по умолчанию не выполняет действий по
отрисовке.  
[DrawCore](M_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_DrawCore.htm)|
Выводим штамп на страницу PDF, для которой задан объект XGraphics. Если штамп
не содержит строк, т.е. свойство
[IsEmpty](P_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_IsEmpty.htm)
вернуло true, то метод в реализации по умолчанию не выполняет действий по
отрисовке.  
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
[GetFont](M_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_GetFont.htm)|
Возвращает шрифт XFont, рекомендуемый для использования при выводе штампов, по
заданному семейству шрифтов familyName и размера шрифта emSize.  
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
[SetFont](M_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter_SetFont.htm)|
Устанавливает текущий шрифт по заданным параметрам.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[AppendDate](M_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensions_AppendDate.htm)|
Добавляет строку с заданной датой в штамп. Дата не конвертируется в локальное
время и выводится как есть.  
(Определяется
[PdfStampExtensions](T_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[Tessa.Extensions.Default.Client.Pdf - пространство
имён](N_Tessa_Extensions_Default_Client_Pdf.htm)
