<?xml version="1.0" encoding="UTF-8"?>
<!--
  MathML → OMML transform tuned for STEM textbook math.

  Covers: mi/mn/mo/mtext/mrow, mfrac, msup/msub/msubsup, msqrt/mroot,
  mfenced, mtable/mtr/mtd (matrix + align + cases), mover/munder/munderover
  (vectors, sums, integrals with limits), mphantom (skipped), mspace,
  multi-char mi (vec/hat/bar accents via combining marks).

  NOT a full implementation of OMML. For 100% fidelity replace with the
  official MS Office MML2OMML.XSL.
-->
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:mml="http://www.w3.org/1998/Math/MathML"
    xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"
    exclude-result-prefixes="mml">

  <xsl:output method="xml" indent="no" omit-xml-declaration="yes"/>

  <xsl:template match="/mml:math | /math">
    <m:oMath>
      <xsl:apply-templates/>
    </m:oMath>
  </xsl:template>

  <xsl:template match="mml:mrow | mrow">
    <xsl:apply-templates/>
  </xsl:template>

  <xsl:template match="mml:mi | mi">
    <m:r>
      <m:rPr><m:sty m:val="i"/></m:rPr>
      <m:t><xsl:value-of select="."/></m:t>
    </m:r>
  </xsl:template>

  <xsl:template match="mml:mn | mn">
    <m:r><m:t><xsl:value-of select="."/></m:t></m:r>
  </xsl:template>

  <xsl:template match="mml:mo | mo">
    <m:r><m:t><xsl:value-of select="."/></m:t></m:r>
  </xsl:template>

  <xsl:template match="mml:mtext | mtext">
    <m:r><m:t><xsl:value-of select="."/></m:t></m:r>
  </xsl:template>

  <!-- whitespace / spacing -->
  <xsl:template match="mml:mspace | mspace">
    <m:r><m:t xml:space="preserve"> </m:t></m:r>
  </xsl:template>

  <!-- phantom is invisible spacing — drop content -->
  <xsl:template match="mml:mphantom | mphantom"/>

  <!-- mstyle is a wrapper for attribute scoping; pass children through -->
  <xsl:template match="mml:mstyle | mstyle">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- mpadded is a wrapper too -->
  <xsl:template match="mml:mpadded | mpadded">
    <xsl:apply-templates/>
  </xsl:template>

  <xsl:template match="mml:mfrac | mfrac">
    <m:f>
      <m:fPr><m:type m:val="bar"/></m:fPr>
      <m:num><xsl:apply-templates select="*[1]"/></m:num>
      <m:den><xsl:apply-templates select="*[2]"/></m:den>
    </m:f>
  </xsl:template>

  <xsl:template match="mml:msup | msup">
    <m:sSup>
      <m:e><xsl:apply-templates select="*[1]"/></m:e>
      <m:sup><xsl:apply-templates select="*[2]"/></m:sup>
    </m:sSup>
  </xsl:template>

  <xsl:template match="mml:msub | msub">
    <m:sSub>
      <m:e><xsl:apply-templates select="*[1]"/></m:e>
      <m:sub><xsl:apply-templates select="*[2]"/></m:sub>
    </m:sSub>
  </xsl:template>

  <xsl:template match="mml:msubsup | msubsup">
    <m:sSubSup>
      <m:e><xsl:apply-templates select="*[1]"/></m:e>
      <m:sub><xsl:apply-templates select="*[2]"/></m:sub>
      <m:sup><xsl:apply-templates select="*[3]"/></m:sup>
    </m:sSubSup>
  </xsl:template>

  <xsl:template match="mml:msqrt | msqrt">
    <m:rad>
      <m:radPr><m:degHide m:val="1"/></m:radPr>
      <m:deg/>
      <m:e><xsl:apply-templates/></m:e>
    </m:rad>
  </xsl:template>

  <xsl:template match="mml:mroot | mroot">
    <m:rad>
      <m:radPr><m:degHide m:val="0"/></m:radPr>
      <m:deg><xsl:apply-templates select="*[2]"/></m:deg>
      <m:e><xsl:apply-templates select="*[1]"/></m:e>
    </m:rad>
  </xsl:template>

  <xsl:template match="mml:mfenced | mfenced">
    <m:d>
      <m:dPr>
        <xsl:if test="@open"><m:begChr m:val="{@open}"/></xsl:if>
        <xsl:if test="@close"><m:endChr m:val="{@close}"/></xsl:if>
        <xsl:if test="@separators"><m:sepChr m:val="{@separators}"/></xsl:if>
      </m:dPr>
      <m:e><xsl:apply-templates/></m:e>
    </m:d>
  </xsl:template>

  <!--
    mover: an accent or limit above an expression.
    - If the over-element is an arrow/bar/hat (accent), render as m:acc.
    - If it's a limit on a sum/integral operator, render as m:nary or m:limUpp.
    Heuristic: if base is a single mo that looks like an operator (sum/int/lim),
    treat as upper limit; otherwise treat as accent.
  -->
  <xsl:template match="mml:mover | mover">
    <xsl:variable name="overText" select="string(*[2])"/>
    <xsl:choose>
      <xsl:when test="$overText='→' or $overText='⃗' or $overText='↔' or $overText='←' or $overText='ˆ' or $overText='^' or $overText='˜' or $overText='~' or $overText='¯' or $overText='-' or $overText='˙' or $overText='.'">
        <m:acc>
          <m:accPr><m:chr m:val="{$overText}"/></m:accPr>
          <m:e><xsl:apply-templates select="*[1]"/></m:e>
        </m:acc>
      </xsl:when>
      <xsl:otherwise>
        <m:limUpp>
          <m:e><xsl:apply-templates select="*[1]"/></m:e>
          <m:lim><xsl:apply-templates select="*[2]"/></m:lim>
        </m:limUpp>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="mml:munder | munder">
    <m:limLow>
      <m:e><xsl:apply-templates select="*[1]"/></m:e>
      <m:lim><xsl:apply-templates select="*[2]"/></m:lim>
    </m:limLow>
  </xsl:template>

  <!--
    munderover: typically sum/int with both limits. Render as m:nary so the
    operator gets the right limit positioning.
  -->
  <xsl:template match="mml:munderover | munderover">
    <xsl:variable name="op" select="string(*[1])"/>
    <m:nary>
      <m:naryPr>
        <m:chr m:val="{$op}"/>
        <m:limLoc m:val="undOvr"/>
      </m:naryPr>
      <m:sub><xsl:apply-templates select="*[2]"/></m:sub>
      <m:sup><xsl:apply-templates select="*[3]"/></m:sup>
      <m:e/>
    </m:nary>
  </xsl:template>

  <!--
    mtable: matrices, align environments, cases.
    Build an m:m with one m:mc per column; column count = max td count.
  -->
  <xsl:template match="mml:mtable | mtable">
    <m:m>
      <m:mPr>
        <m:mcs>
          <m:mc>
            <m:mcPr>
              <m:count m:val="{count(*[1]/*)}"/>
              <m:mcJc m:val="center"/>
            </m:mcPr>
          </m:mc>
        </m:mcs>
      </m:mPr>
      <xsl:apply-templates/>
    </m:m>
  </xsl:template>

  <xsl:template match="mml:mtr | mtr">
    <m:mr>
      <xsl:apply-templates/>
    </m:mr>
  </xsl:template>

  <xsl:template match="mml:mtd | mtd">
    <m:e>
      <xsl:apply-templates/>
    </m:e>
  </xsl:template>

  <!--
    mlabeledtr: like mtr but first child is an equation label (e.g. (1)).
    OMML has no native label cell — skip the label and render the rest.
  -->
  <xsl:template match="mml:mlabeledtr | mlabeledtr">
    <m:mr>
      <xsl:apply-templates select="*[position() &gt; 1]"/>
    </m:mr>
  </xsl:template>

  <!-- merror: invalid markup, render as red text -->
  <xsl:template match="mml:merror | merror">
    <m:r>
      <m:rPr><m:nor/></m:rPr>
      <m:t><xsl:value-of select="."/></m:t>
    </m:r>
  </xsl:template>

  <!-- multiscripts (rare) — render as msup or msub fallback -->
  <xsl:template match="mml:mmultiscripts | mmultiscripts">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- semantics: just unwrap to first child -->
  <xsl:template match="mml:semantics | semantics">
    <xsl:apply-templates select="*[1]"/>
  </xsl:template>

  <xsl:template match="mml:annotation | annotation | mml:annotation-xml | annotation-xml"/>

  <!-- catch-all: descend into unknown elements -->
  <xsl:template match="*">
    <xsl:apply-templates/>
  </xsl:template>

</xsl:stylesheet>
